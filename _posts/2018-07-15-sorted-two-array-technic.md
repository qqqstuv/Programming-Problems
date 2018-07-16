---
layout: post
title: Synchronized Sorting two list problem
categories: [array, tutorial]
tags: [array, sorted, binarysearch]
fullview: false
comments: true
---

### whenever you need to do searching in two synchronized list, maybe think of using this technic 

Example of problems:
[Most profit in assigning work](https://leetcode.com/problems/most-profit-assigning-work/description/),
[Longest Increasing Subsequence ](https://leetcode.com/problems/longest-increasing-subsequence/description/)

Looking at Most Profit in Assigning Work: for each worker, we would like to find out (search) all the difficulty that the worker can handle but at the same time we would like to choose (search) for the most profit that worker can achieve.
The tricky part is if we sort the difficulty then searching in difficulty takes log(n) but searching for most profit takes O(n). At the same time if we sort profit, searching for difficulty takes O(n). Overall the brute force time would be O(n^2)

The sorting technic comes into play when we keep one list (difficulty) sorted and try to convert the other list into a sorted array to reduce search time to O(log(n))


<!-- **dbyll** is minimalist, stylish theme for jekyll. Supports gravatar, account links (github, twitter, e-mail, pinterest, résume file) and a bio.  

**dbyll** is brought to you by **[dbtek](http://ismaildemirbilek.com)**. Open sourced under [MIT](http://opensource.org/licenses/MIT) license. -->

<!-- ### dbyll is on GitHub

<a class="btn btn-default" href="https://github.com/dbtek/dbyll">Grab your copy now!</a> -->
