#!/usr/bin/env wolframscript
(* ::Package:: *)

ANSWER = 4037526;
LIMIT = 5 * 10 ^ 15;

sq2 = (LIMIT / 2) ^ 0.5;
k = 1; S = 0;
While[ k < sq2,
	If[PrimeQ[2 * k * k + 2 * k + 1], S += 1];
	k += 1;
]
S
