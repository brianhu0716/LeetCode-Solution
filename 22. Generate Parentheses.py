# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:41:59 2021

@author: brian.hu
"""
"""
at any state, the number of "(" must always greater than number of ")"
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(res,nl,nr) :
            """
            Parameters
            ----------
            res : list[str]
                record every possible combination state 
            nl : int
                number of left bracket at current state
            nr : int
                number of right bracket at current state

            Returns
            -------
            None.

            """
            if nr > nl : return # at any state, we can't let # of ")" greater than # of "("
            
            if len(res) == 2 * n : # find an answer
                self.ans += [res[:]]
                return 
            
            # if # of "(" greater than # of ")", we can choose either add a "(" or a ")" in current combination
            if nl > nr : 
                if nl < n : 
                    dfs(res + "(" ,nl + 1,nr)
                    dfs(res + ")" ,nl,nr + 1)
                else: # we've already put the maximum # of "(" in combination, thus we can only put ")" in next state
                    dfs(res + ")",nl,nr + 1)
            elif nl == nr :
                dfs(res + "(",nl + 1,nr)
                
        self.ans = list()
        dfs("",0,0)
        return self.ans