import Data.List
import System.IO
import Data.Ord
import Data.Monoid
import Data.List.Split

compareTuples :: (Ord a, Ord b) => (a, b) -> (a, b) -> Ordering
compareTuples (a,b) (c,d) = 
	case compare c a  of 
		EQ -> compare b d
		ne -> ne
getCheck line = last $ splitOn "-" line
getWords line = concat $ init $ splitOn "-" line
getPass line = splitOn "-" $ head ( init $ splitOn "[" line )  --should take everything except []

frequencyOfLetters letts = map (\x -> (length x, head x)) (group  $sort (filter (/='-') letts))

take2 = map snd

rotLetter 0 l = l
rotLetter i 'z' = rotLetter (i - 1) 'a' 
rotLetter i l = rotLetter (i-1)(succ l) 

checkCode line = first == second
	where first = take 5 $ take2 $ sortBy compareTuples (frequencyOfLetters $ getWords line)
	      second = init $ splitOn "[" (getCheck line) !! 1

main = do	
	content <- readFile "day4.in"
	let a = filter checkCode (lines content)
	print $ sum $  map (\x -> read (splitOn "[" x !! 0) :: Int) $ map getCheck a
	let decoded =  map (\x -> map (rotLetter (read (last x) :: Int)) (unwords $ init x)) (map getPass a)
	print $ elemIndex (head $ filter (\x -> "north" == take 5 x) decoded) decoded
	print $ a !! 466 --I'm lazy
