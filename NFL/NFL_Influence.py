#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:12:10 2022

@author: jacobelder
"""
import numpy as np 
import pandas as pd
import praw #for reddit wrapper
import matplotlib.pyplot as plt #for basic visualizations
import networkx as nx #to create Network Graphs

#Setting up the Reddit API in python
reddit = praw.Reddit(client_id='Your Client ID',
                     client_secret='Your Client Secret',
                     user_agent='User')

def get_posts(subred_name, n):
    subreddit = reddit.subreddit(subred_name)
    posts_info = [] 
    
    for subm in subreddit.top(limit=n):
        
        subred_info = []
        subred_info.append(subm.id)  
        subred_info.append(str(subm.author)) 
        subred_info.append(subm.score)  
        subred_info.append(subm.upvote_ratio)
        subred_info.append(subm.num_comments)
        subred_info.append(subm.subreddit)
        posts_info.append(subred_info)
    
    sorted_info = sorted(posts_info, key=lambda x: x[1], reverse = True)
    posts_df = pd.DataFrame(sorted_info, columns = ['id','author', 'score','upvote_ratio' ,'num_comments', 'subreddit'])
    return posts_df