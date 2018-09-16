"""
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".


"""

'''
# not correct

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stk = []
        for s in path:
            if not stk:
                stk.append(s)
                continue
            if stk[-1] == '/' and s == '/': continue
            if stk[-1] == '/' and s == '.':
                stk.pop()
                if not stk:
                    stk.append('/')
                    continue
                while stk[-1] != '/': stk.pop()
                continue
            if stk[-1] == '.' and s == '.':
                stk = []
                continue
            stk.append(s)
        if len(stk) > 1:
            stk.pop()
        return ''.join(stk)
                   

'''


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stk = []
        path = path.split('/')
        for s in path:
            if s == '' or s == '.': continue
            if s == '..':
                if stk: stk.pop()
                continue
            stk.append(s)
        return '/' + '/'.join(stk)

