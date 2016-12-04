import System.IO
import Data.List

isViableTriangle :: [Int] -> Bool
isViableTriangle (a:b:c:[]) = (a+b) > c

getInts :: [String] -> [Int]
getInts words' =  map (\x -> read x :: Int) words'

getColumn ints index = map (\x -> x !! index) ints

wholeList ints = getColumn ints 0 ++ getColumn ints 1 ++ getColumn ints 2

groupsOf3 [] = []
groupsOf3 (a:b:c:xs) = [a,b,c] : groupsOf3 xs

main = do
	content <- readFile "day3.in"
	let linesOfFile = lines content
	let wordsOfFile = map words linesOfFile
	let ints = map getInts wordsOfFile
	print $ length $ filter isViableTriangle (map sort ints) 
	print $ length $ filter isViableTriangle (map sort(groupsOf3 $ wholeList ints))

