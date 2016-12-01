--Haskell solution
import System.IO

let directions = "NESW"

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

--main = do
--	handle <- openFile "day1.in" ReadMode
--	contents <- hGetContents handle
--	let parsedInput = map (filter (/=','))  (words $ init contents)
