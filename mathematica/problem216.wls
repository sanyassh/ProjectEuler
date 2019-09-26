#!/usr/bin/env wolframscript
(* ::Package:: *)

ANSWER = 5437849;
LIMIT = 50 * 10 ^ 6;

n = 1; S = 0;
While[ n <= LIMIT,
	If[PrimeQ[2 * n ^ 2 - 1], S += 1];
	n += 1;
]
S
