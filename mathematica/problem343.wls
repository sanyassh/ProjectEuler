#!/usr/bin/env wolframscript
(* ::Package:: *)

ANSWER = 269533451410884183;
LIMIT = 2 * 10 ^ 6;

n = 1;
S = 0;
While[ n <= LIMIT,
	num = n * n - n + 1;
	fm = FactorInteger[num];
	m = Max[fm[[{-1}, 1]]];
	fmn = FactorInteger[n + 1];
	mn = Max[fmn[[{-1}, 1]]];
	S += Max[m, mn] - 1;
	n += 1;
];
S
