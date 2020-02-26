#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:21:53 2020

@author: Steve Satterfield
"""

STYLE_NORMAL = "Normal"
STYLE_BODY_TEXT = "Body Text"

BLOOM_ACTION_WORDS = ["learn","read","arrange","define","describe","duplicate","identify","label","list","match","memorize","name","order","outline",
                      "recognize","relate","recall","repeat","reproduce","select","state","explain","summarize","paraphrase","describe",
                      "illustrate","classify","convert","defend","describe","discuss","distinguish","estimate","explain","express","extend",
                      "generalized","give example","give examples","identify","indicate","infer","locate","paraphrase","predict","recognize",
                      "rewrite","review","select","summarize","translate","use","compute","solve","demonstrate","apply","construct","apply",
                      "change","choose","compute","demonstrate","discover","dramatize","employ","illustrate","interpret","manipulate","modify",
                      "operate","practice","prepare","produce","relate","schedule","show","sketch","solve","write",
                      "analyze","categorize","compare","contrast","separate","apply","change","discover","choose","compute","demonstrate",
                      "dramatize","employ","illustrate","interpret","manipulate","modify","operate","prepare","produce",
                      "relate","schedule","show","sketch","solve","write","create","design","hypothesize","invent","develop","arrange",
                      "assemble","categorize","collect","combine","comply","compose","construct","design","develop","devise","explain",
                      "formulate","generate","plan","prepare","rearrange","reconstruct","relate","reorganize","revise","rewrite","set up",
                      "summarize","synthesize","tell","write","judge","recommend","critique","justify","appraise","argue","assess","attach",
                      "choose","compare","conclude","contrast","defend","describe","discriminate","estimate","evaluate","explain","judge",
                      "justify","interpret","relate","predict","rate","select","summarize","support","value","educate","talk","gain",
                      "answer","celebrate","enjoy","stay","avoid","socialize","visit","journey","tour","join","share","knowledge","plan",
                      "option","options","isolation","social","author","literary","social","find"]

BLOOM_ACTION_STEMS = ["abus","achiev","adventur","analysi","anxieti","learn","read","arrange","define","describe","duplicate","identify",
                      "label","list","match","memorize","name","order","outline","explor","research","volunt","entertain","handicap"]

BLOOM_ACTION_VERBS = ["learn","read","arrange","define","describe","duplicate","identify","label","list","match","memorize","name","order","outline",
                      "recognize","relate","recall","repeat","reproduce","select","state","explain","summarize","paraphrase","describe",
                      "illustrate","classify","convert","defend","describe","discuss","distinguish","estimate","explain","express","extend",
                      "generalized","give example","give examples","identify","indicate","infer","locate","paraphrase","predict","recognize",
                      "rewrite","review","select","summarize","translate","use","compute","solve","demonstrate","apply","construct","apply",
                      "change","choose","compute","demonstrate","discover","dramatize","employ","illustrate","interpret","manipulate","modify",
                      "operate","practice","predict","prepare","produce","relate","schedule","show","sketch","solve","write",
                      "analyze","categorize","compare","contrast","separate","apply","change","discover","choose","compute","demonstrate",
                      "dramatize","employ","illustrate","interpret","manipulate","modify","operate","practice","predict","prepare","produce",
                      "relate","schedule","show","sketch","solve","write","create","design","hypothesize","invent","develop","arrange",
                      "assemble","categorize","collect","combine","comply","compose","construct","design","develop","devise","explain",
                      "formulate","generate","plan","prepare","rearrange","reconstruct","relate","reorganize","revise","rewrite","set up",
                      "summarize","synthesize","tell","write","judge","recommend","critique","justify","appraise","argue","assess","attach",
                      "choose","compare","conclude","contrast","defend","describe","discriminate","estimate","evaluate","explain","judge",
                      "justify","interpret","relate","predict","rate","select","summarize","support","value","educate","talk","gain",
                      "answer","celebrate","enjoy","stay","avoid","socialize","visit","journey","tour","join","share","plan",
                      "isolation","social","author","social","find"]

LL_NOUNS = ["share","knowledge","plan","option","options","isolation","author","social","journey","goals","trauma","tinnitus","trauma","treatment","counseling","information",
            "planetarium","presentation","plan","explaination","diversification","portfolio","strategies","planning","taxes","tax-advantaged investments","opportunity",
            "demonstration","tour","conservation","restoration","craftsmanship","tactics","preparedness","Renaissance","impediments","overview","self-edit","traditions",
            "example","violence","religion","analysis","disciplines","evidence","toxicology","discipline","disciplines","analysis","history"]

LL_ADJECTIVES = ["social","literary","actionable","historical","environmental"]

LL_PHRASES = ["stay active","stay active and engaged","social isolation","get started volunteering",
              "find out why","find out how","learn how","learn why","share his knowledge","share her knowledge",
              "enlighten class participants","plans to tell us about","rise to power","learn about","intervention services","health needs",
              "develop strategies","crisis situations","dealing with","lessen trauma","help seniors","department of elder affairs","medicare fraud",
              "a tour of the campus","financial impact","emotional impact","why planning","actionable strategies","cash management","retirement income","lifelong learner",
              "retirement planning counselor","retirement planning","improve business","job opportunities","participants requested","inviting us back",
              "national register of historical places","tap room","local artists","local artist","local ingredients","community preparedness","educate the community",
              "personal responsibility","self-sufficiency","reducing the vulnerability","changes in society","learn about the history","race relations",
              "paths forward","how do we account","safety issues","safety and security","friend of leisure learning","share the history","play the popular game","fresh air and sun",
              "modest exercise","create new friends","enjoyable way","moderate rewards","substantial risks","great oratory","public discourse","reasoned argument",
              "principles of justice","representative government","public institutions","impacts your health","biological rhythm","leading edge","bleeding edge",
              "engage your thinking","active discussion","all participants","continue to suffer","political belief system","did you know","crime scene","ever had the desire",
              "an introduction to"]

LL_JUNKS = ["avoid","engaged","find","volunteer","participate","tell","prevent","lessen","lessened","specializes","plan","invited","involve","join","aspire","transformed",
            "amplified","discussing"]

LL_VERBS = ["avoid"]

LL_NOUNS_REQUIRE_QUALIFIER = ["solution"]

STYLE_KNOWLEDGEAREA = "Normal"

COORDINATING_CONJUNCTION = "CC"
CARDINAL_DIGIT = "CD"
DETERMINER = "DT"
EXISTENTIAL_THERE = "EX"
FOREIGN_WORD = "FW"
PREPOSITION_COORDINATING_CONJUNCTION = "IN"
ADJECTIVE = "JJ"
ADJECTIVE_COMPARATIVE = "JJR"
ADJECTIVE_SUPERLATIVE = "JJS"
LIST_MARKER = "LS"
MODAL = "MD"
NOUN_SINGULAR = "NN"
NOUN_PLURAL = "NNS"
NOUN_PROPER_SINGULAR = "NNP"
NOUN_PROPER_PLURAL = "NNPS"
PREDETERMINER = "PDT"
POSSESSIVE = "POS"
PRONOUN_PERSONAL = "PRP"
PRONOUN_POSSESSIVE = "PRP$"
ADVERB = "RB"
ADVERB_COMPARATIVE = "RBR"
ADVERB_SUPERLATIVE = "RBS"
PARTICIPLE = "RP"
TO_GO = "TO"
INTERJECTION = "UH"
VERB = "VB"
VERB_PAST_TENSE = "VBD"
VERB_GERUND = "VBG"
VERB_PAST_PARTICIPLE = "VBN"
VERB_SINGULAR_PRESENT = "VBP"
VERB_THIRD_PERSON_SINGULAR = "VBZ"
WH_DETERMINER = "WDT"
WH_PRONOUN = "WP"
WH_PRONOUN_POSSESSIVE = "WP$"
WH_ADVERB = "WRB"