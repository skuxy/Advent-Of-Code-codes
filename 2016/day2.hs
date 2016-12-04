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

length' keypad index = sum ( map (\x -> if (x !! index) == '-' then 0 else 1) keypad)

moveKey 'U' (a,b) keypad'' = if a `elem` [1..length keypad''-1] then decY (a,b) else (a,b)
moveKey 'D' (a,b) keypad'' = if a `elem` [0..length keypad''-2] then incY (a,b) else (a,b)
moveKey 'R' (a,b) keypad'' = if b `elem` [0..length (keypad'' !! a )- 2] then incX (a,b) else (a,b)
moveKey 'L' (a,b) keypad'' = if b `elem` [1..length (keypad'' !! a )- 1] then decX (a,b) else (a,b)

parseLine [] point _  = point
parseLine (x:xs) point keypad'' = parseLine xs (moveKey x point keypad'') keypad''

main = do
	content <- readFile "day2.in" 
	let linesOfFile = lines content
	let keys = map elemKeypad (map (\x -> parseLine x (1,1) keypad) linesOfFile)
	print keys
