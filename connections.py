# posuđeni dio koda koji se zapravo vrti u beskonačnim rekurzijama, potrebno modificirati

import ast, itertools, os
import re, importlib
import collections

class Connections:
    def __init__(self):
        self._classes, self.edges = {}, []
    def walk(self, t, scope=None):
        d = collections.deque([(t, None)])
        while d:
            t_obj, [tree, scope] = None, d.popleft()
            if isinstance(tree, ast.ClassDef):
                self._classes[tree.name] = [i for i in tree.body if isinstance(i, ast.FunctionDef) and not re.findall('__[a-z]+__', i.name)]
                d.extend([(i, [tree.name, i.name]) for i in self._classes[tree.name]])
                t_obj = [i for i in tree.body if i not in self._classes[tree.name]]
            elif isinstance(tree, (ast.Import, ast.ImportFrom)):
                for p in [tree.module] if hasattr(tree, 'module') else [i.name for i in tree.names]:
                    try:
                        if (p1:=getattr(importlib.import_module(p), '__file__', None)) is not None:
                            if not p1.startswith('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10'):
                                with open(p1) as f:
                                    try:
                                        t_obj = ast.parse(f.read())
                                    except:
                                        pass
                    except:
                        pass
            elif isinstance(tree, ast.Attribute) and scope is not None:
                if (c:=[a for a, b in self._classes.items() if any(i.name == tree.attr for i in b)]):
                    self.edges.append((scope, [c[0], tree.attr]))
                t_obj = tree.value
            if isinstance(t_obj:=(tree if t_obj is None else t_obj), list):
                for i in t_obj:
                    d.append((i, scope))
            else:
                for i in getattr(t_obj, '_fields', []):
                    d.append((getattr(t_obj, i), scope))