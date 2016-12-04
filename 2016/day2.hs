--Day two, part one and two

import System.IO

type Keypad = [[Char]]
keypad = [['1','2','3'],['4','5','6'],['7','8','9']]
keypad' = ["--1--","-234-","56789","-ABC-","--D--"]

type Point = (Int,Int)
point = (1,1)

elemKeypad (y,x) = keypad !! y !! x
elemKeypad' (y,x) = keypad' !! y !! x

incY (a,b) = (a+1,b)
incX (a,b) = (a,b+1)
decY (a,b) = (a-1,b)
decX (a,b) = (a,b-1)

nOfDashesX keypad'' index = length $ filter (=='-') (keypad'' !! index)
nOfDashesY keypad'' index = length $ filter (=='-') (map (\x -> x !! index) keypad'')
nOfStuffX keypad'' index = length $ filter (/='-') (keypad'' !! index)
nOfStuffY keypad'' index = length $ filter (/='-') (map (\x -> x !! index) keypad'')

moveKey 'U' (a,b) keypad'' = if a `elem` (tail $ init [begin..begin+end]) then decY (a,b) else (a,b)
	where begin = (nOfDashesY keypad'' b) `div` 2
	      end = nOfStuffY keypad'' b
moveKey 'D' (a,b) keypad'' = if a `elem` (init $ init [begin..begin+end]) then incY (a,b) else (a,b)
	where begin = (nOfDashesY keypad'' b) `div` 2
	      end = nOfStuffY keypad'' b
moveKey 'R' (a,b) keypad'' = if b `elem` (init $ init [begin..begin+end]) then incX (a,b) else (a,b)
	where begin = (nOfDashesX keypad'' a) `div` 2
	      end = nOfStuffX keypad'' a
moveKey 'L' (a,b) keypad'' = if b `elem` (tail $ init [begin..begin+end]) then decX (a,b) else (a,b)
	where begin = (nOfDashesX keypad'' a) `div` 2
	      end = nOfStuffX keypad'' a

parseLine [] point _  = point
parseLine (x:xs) point keypad'' = parseLine xs (moveKey x point keypad'') keypad''

main = do
	content <- readFile "day2.in" 
	let linesOfFile = lines content
	let keys = map elemKeypad (map (\x -> parseLine x (1,1) keypad) linesOfFile)
	let keys2 = map elemKeypad' (map (\x -> parseLine x (2,0) keypad') linesOfFile)
	print keys
	print keys2
