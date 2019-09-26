#!/usr/bin/env wolframscript
(* ::Package:: *)

ANSWER = 18613426663617118;
LIMIT = 10 ^ 6;

S = 0; p = 5; q = 7;
While[ p < LIMIT,
	S += ChineseRemainder[
		{0, p},
		{q, 10 ^ (Floor[Log[10, p]] + 1)}
	];
	p = q;
	q = NextPrime[q];
]
S
