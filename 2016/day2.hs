--Day two, part one

import System.IO

type Keypad = [[Int]]
keypad = [[1,2,3],[4,5,6],[7,8,9]]

type Point = (Int,Int)
point = (1,1)

elemKeypad (y,x) = keypad !! y !! x

incY (a,b) = (a+1,b)
incX (a,b) = (a,b+1)
decY (a,b) = (a-1,b)
decX (a,b) = (a,b-1)

moveKey 'U' (a,b) = if a `elem` [1,2] then decY (a,b) else (a,b)
moveKey 'D' (a,b) = if a `elem` [0,1] then incY (a,b) else (a,b)
moveKey 'R' (a,b) = if b `elem` [0,1] then incX (a,b) else (a,b)
moveKey 'L' (a,b) = if b `elem` [1,2] then decX (a,b) else (a,b)

parseLine [] point = point
parseLine (x:xs) point = parseLine xs (moveKey x point)

main = do
	content <- readFile "day2.in" 
	let linesOfFile = lines content
	let keys = map elemKeypad (map (\x -> parseLine x (1,1)) linesOfFile)
	print keys
