#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import re
import os, sys
import math
import pickle
import csv
import collections

def log(n):
    if n != 0:
        return math.log(n, 2)
    else:
        return 0
def PMI(x,y,xy,T):
	if x==0 or y == 0:
		return 0
	else:
		return log(T*xy/(x*y))

def main():

	### Inputs ###
	
	tweet = sys.argv[1] # tweets file
	token = sys.argv[2] # tokens file
	word_pos  = sys.argv[3] # set of positive words
	word_neg  = sys.argv[4] # set of negative words
	output  = sys.argv[5] # output file
	
	### Variables
	
	c_token = collections.Counter() # counter for words
	c_pos = collections.Counter() # counter for positive words
	c_neg = collections.Counter() # counter for negative words
	token_set = set() #  tokens set
	tweet_set = set() # tweets set
	word_pos_set  = set() # set of positive words
	word_neg_set  = set() # set of negative words
	N = 0 # number of words in all tweets
	score = {} # dictionary with results
	
	emoticon = {
	"EMO_HAPPY": ":-)\n:)\n:o)\n:]\n:3\n:c)\n:>\n=]\n8)\n=)\n:}\n:^)\n:-))",
	"EMO_LAUGH": ":-D\n:D\n8-D\n8D\nx-D\nxD\nX-D\nXD\n=-D\n=D\n=-3\n=3\nB^D",
	"EMO_SAD": ">:[\n:-(\n:(\n:-c\n:c\n:-<\n:?C\n:<\n:-[\n:[\n:{",
	"EMO_ANGRY": ":-||\n:@",
	"EMO_CRYING": ":'-(\n:'(\nQQ",
	"EMO_TEARS": ":'-)\n:')",
	"EMO_HEART": "<3\n</3",
	"EMO_HORROR": "D:<\nD:\nD8\nD;\nD=\nDX\nv.v\nD-':",
	"EMO_SURPRISE": ">:O\n:-O\n:O\n°o°\n°O°\n:O\no_O\no_0\no.O\n8-0",
	"EMO_KISS": ":*\n:^*\n'}{'",
	"EMO_WINK": ";-)\n;)\n*-)\n*)\n;-]\n;]\n;D\n;^)\n:-,",
	"EMO_CHEEKY": ">:P\n:-P\n:P\nX-P\nx-p\nxp\nXP\n:-p\n:p\n=p\n:-Þ\n:Þ\n:-b\n:b",
	"EMO_SKEPTICAL": ">:\\\n>:/\n:-/\n:-.\n:/\n:\\\n=/\n=\\\n:L\n=L\n:S\n>.<",
	"EMO_INDECISION": ":-|",
	"EMO_EMBARASSED": ":$",
	"EMO_SEALED": ":-X\n:X\n:-#\n:#",
	"EMO_ANGEL": "O:-)\n0:-3\n0:3\n0:-)\n0:)\n0;^)",
	"EMO_EVIL": ">:)\n>;)\n>:-)",
	"EMO_DEVIL": "}:-)\n}:)\n3:-)\n3:)",
	"EMO_HIGH5": "o/\\o\n^5\n>_>^\n^<_<",
	"EMO_COOL": "|;-)\n|-O"
	}
    
	
	
	
	
	# Read and input frequency
    
	for line in open(token, "r"):
		token_set.add(line.replace("\n",""))
    
	for line in open(tweet, "r"):
		tweet_set.add(line.replace("\n",""))
		
	for line in open(word_pos, "r"):
		word_pos_set.add(line.replace("\n",""))
	
	for line in open(word_neg, "r"):
		word_neg_set.add(line.replace("\n",""))
		
	#for tweet in tweet_set:
		# N += len(tweet.split())
	N = len(tweet_set)	

	# Positive and negative words frequency in tweet set
	for tweet in tweet_set:
		words_in_tweet = tweet.split()
		for word in word_pos_set:
			if word in words_in_tweet:
				c_pos[word] +=1				
		for word in word_neg_set:
			if word in words_in_tweet:
				c_neg[word] +=1		
	
	# Tokens and bigrams frequency in tweet set
	for word in token_set:
		c_word_p = collections.Counter() # Bigram frequency (positive set)
		c_word_n = collections.Counter() # Bigram frequency (negative set)
		PMI_pos = 0
		PMI_neg = 0
		for tweet in tweet_set:
			words_in_tweet = tweet.split()
			# Managing emoticon in token
			if word in emoticon.keys():
				for supp in emoticon[word].split():
					if supp in words_in_tweet:
						c_token[word] +=1
						for p in word_pos_set:
							if supp in tweet.split() and p in words_in_tweet:
								c_word_p[word+p] += 1
						for n in word_neg_set:
							if supp in tweet.split() and n in words_in_tweet:
								c_word_n[word+n] += 1
			else:
				if word in words_in_tweet:
					c_token[word] +=1
				for p in word_pos_set:
					if word in words_in_tweet and p in words_in_tweet:
						c_word_p[word+p] += 1
				for n in word_neg_set:
					if word in words_in_tweet and n in words_in_tweet:
						c_word_n[word+n] += 1
		# PMI score
		for p in word_pos_set:
			PMI_pos += PMI(c_token[word],c_pos[p],c_word_p[word+p],N)
		for n in word_neg_set:
			PMI_neg += PMI(c_token[word],c_neg[n],c_word_n[word+n],N)	
		score[word] = [c_token[word],PMI_pos-PMI_neg, PMI_pos, PMI_neg]
			
	### Save result ###       
    
	w = csv.writer(open(output, "w"))
	for key, val  in score.items():
		w.writerow([key, val])

main()
