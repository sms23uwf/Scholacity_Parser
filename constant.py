#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:21:53 2020

@author: claudiasatterfield
"""

STYLE_NORMAL = "Normal"
STYLE_BODY_TEXT = "Body Text"

BLOOM_ACTION_WORDS = ["read","arrange","define","describe","duplicate","identify","label","list","match","memorize","name","order","outline",
                      "recognize","relate","recall","repeat","reproduce","select","state","explain","summarize","paraphrase","describe",
                      "illustrate","classify","convert","defend","describe","discuss","distinguish","estimate","explain","express","extend",
                      "generalized","give example","give examples","identify","indicate","infer","locate","paraphrase","predict","recognize",
                      "rewrite","review","select","summarize","translate","use","compute","solve","demonstrate","apply","construct","apply",
                      "change","choose","compute","demonstrate","discover","dramatize","employ","illustrate","interpret","manipulate","modify",
                      "operate","practice","predict","prepare","produce","relate","schedule","show","sketch","solve","use","write",
                      "analyze","categorize","compare","contrast","separate","apply","change","discover","choose","compute","demonstrate",
                      "dramatize","employ","illustrate","interpret","manipulate","modify","operate","practice","predict","prepare","produce",
                      "relate","schedule","show","sketch","solve","use","write","create","design","hypothesize","invent","develop","arrange",
                      "assemble","categorize","collect","combine","comply","compose","construct","create","design","develop","devise","explain",
                      "formulate","generate","plan","prepare","rearrange","reconstruct","relate","reorganize","revise","rewrite","set up",
                      "summarize","synthesize","tell","write","judge","recommend","critique","justify","appraise","argue","assess","attach",
                      "choose","compare","conclude","contrast","defend","describe","discriminate","estimate","evaluate","explain","judge",
                      "justify","interpret","relate","predict","rate","select","summarize","support","value","educate","talk","gain",
                      "answer","celebrate","enjoy","stay","avoid","socialize","visit","journey","tour","join","share","knowledge","plan",
                      "options","isolation","social","author","literary","social","find"]

BLOOM_ACTION_VERBS = ["read","arrange","define","describe","duplicate","identify","label","list","match","memorize","name","order","outline",
                      "recognize","relate","recall","repeat","reproduce","select","state","explain","summarize","paraphrase","describe",
                      "illustrate","classify","convert","defend","describe","discuss","distinguish","estimate","explain","express","extend",
                      "generalized","give example","give examples","identify","indicate","infer","locate","paraphrase","predict","recognize",
                      "rewrite","review","select","summarize","translate","use","compute","solve","demonstrate","apply","construct","apply",
                      "change","choose","compute","demonstrate","discover","dramatize","employ","illustrate","interpret","manipulate","modify",
                      "operate","practice","predict","prepare","produce","relate","schedule","show","sketch","solve","use","write",
                      "analyze","categorize","compare","contrast","separate","apply","change","discover","choose","compute","demonstrate",
                      "dramatize","employ","illustrate","interpret","manipulate","modify","operate","practice","predict","prepare","produce",
                      "relate","schedule","show","sketch","solve","use","write","create","design","hypothesize","invent","develop","arrange",
                      "assemble","categorize","collect","combine","comply","compose","construct","create","design","develop","devise","explain",
                      "formulate","generate","plan","prepare","rearrange","reconstruct","relate","reorganize","revise","rewrite","set up",
                      "summarize","synthesize","tell","write","judge","recommend","critique","justify","appraise","argue","assess","attach",
                      "choose","compare","conclude","contrast","defend","describe","discriminate","estimate","evaluate","explain","judge",
                      "justify","interpret","relate","predict","rate","select","summarize","support","value","educate","talk","gain",
                      "answer","celebrate","enjoy","stay","avoid","socialize","visit","journey","tour","join","share","knowledge","plan",
                      "options","isolation","social","author","literary","social","find"]

BLOOM_NOUNS = ["read","arrange","define","describe","duplicate","identify","label","list","match","memorize","name","order","outline",
               "recognize","relate","recall","repeat","reproduce","select","state","explain","summarize","paraphrase","describe",
               "illustrate","classify","convert","defend","describe","discuss","distinguish","estimate","explain","express","extend",
               "generalized","give example","give examples","identify","indicate","infer","locate","paraphrase","predict","recognize",
               "rewrite","review","select","summarize","translate","use","compute","solve","demonstrate","apply","construct","apply",
               "change","choose","compute","demonstrate","discover","dramatize","employ","illustrate","interpret","manipulate","modify",
               "operate","practice","predict","prepare","produce","relate","schedule","show","sketch","solve","use","write",
               "analyze","categorize","compare","contrast","separate","apply","change","discover","choose","compute","demonstrate",
               "dramatize","employ","illustrate","interpret","manipulate","modify","operate","practice","predict","prepare","produce",
               "relate","schedule","show","sketch","solve","use","write","create","design","hypothesize","invent","develop","arrange",
               "assemble","categorize","collect","combine","comply","compose","construct","create","design","develop","devise","explain",
               "formulate","generate","plan","prepare","rearrange","reconstruct","relate","reorganize","revise","rewrite","set up",
               "summarize","synthesize","tell","write","judge","recommend","critique","justify","appraise","argue","assess","attach",
               "choose","compare","conclude","contrast","defend","describe","discriminate","estimate","evaluate","explain","judge",
               "justify","interpret","relate","predict","rate","select","summarize","support","value","educate","talk","gain",
               "answer","celebrate","enjoy","stay","avoid","socialize","visit","journey","tour","join","share","knowledge","plan",
               "options","isolation","social","author","literary","social","find"]



