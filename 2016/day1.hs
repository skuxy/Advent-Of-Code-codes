--Haskell solution
--part 1
import System.IO

parseDirection :: String -> (Int, Int, Char) -> (Int, Int, Char)
parseDirection (n:xs) (x,y,'N') 
    | n == 'R' = (x + read xs :: Int , y, 'E')
    | n == 'L' = (x - read xs :: Int , y, 'W')

parseDirection (n:xs) (x,y,'E') 
    | n == 'R' = (x, y - read xs :: Int , 'S')
    | n == 'L' = (x, y + read xs :: Int , 'N')

parseDirection (n:xs) (x,y,'S')
    | n == 'R' = (x - read xs :: Int, y, 'W')
    | n == 'L' = (x + read xs :: Int, y, 'E')

parseDirection (n:xs) (x,y,'W')
    | n == 'R' = (x, y + read xs :: Int , 'N')
    | n == 'L' = (x, y - read xs :: Int , 'S')

parseList :: (Int,Int,Char) -> [String] -> (Int,Int,Char)
parseList point [] = point
parseList point (x:xs) = parseList (parseDirection x point)  xs

getManhattan (x,y,_) = (abs x) + (abs y)

--part2

getAllPointsVisited (n:xs) (x,y,'N') 
    | n == 'R' = [(x + i :: Int , y) | i <- [0..read xs :: Int] ]
    | n == 'L' = [(x - i :: Int , y) | i <- [0..read xs :: Int] ]
getAllPointsVisited (n:xs) (x,y,'E') 
    | n == 'R' = [(x, y - i :: Int) | i <- [0..read xs :: Int] ]
    | n == 'L' = [(x, y + i :: Int) | i <- [0..read xs :: Int] ]
getAllPointsVisited (n:xs) (x,y,'S') 
    | n == 'R' = [(x - i :: Int , y) | i <- [0..read xs :: Int] ]
    | n == 'L' = [(x + i :: Int , y) | i <- [0..read xs :: Int] ]
getAllPointsVisited (n:xs) (x,y,'W') 
    | n == 'R' = [(x, y + i :: Int) | i <- [0..read xs :: Int] ]
    | n == 'L' = [(x, y - i :: Int) | i <- [0..read xs :: Int] ]

main = do
	handle <- openFile "day1.in" ReadMode
	contents <- hGetContents handle
	let parsedInput = map (filter (/=','))  (words $ init contents)
        let finalPoint = parseList (0,0,'N') parsedInput
	print $ getManhattan finalPoint


