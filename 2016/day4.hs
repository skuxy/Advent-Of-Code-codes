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

frequencyOfLetters letts = map (\x -> (length x, head x)) (group  $sort (filter (/='-') letts))

take2 = map snd

shiftLetter 'z' = 'a'
shiftLetter l = next l

checkCode line = first == second
	where first = take 5 $ take2 $ sortBy compareTuples (frequencyOfLetters $ getWords line)
	      second = init $ splitOn "[" (getCheck line) !! 1

main = do
	content <- readFile "day4.in"
	let a = filter checkCode (lines content)
	print $ sum $  map (\x -> read (splitOn "[" x !! 0) :: Int) $ map getCheck a
