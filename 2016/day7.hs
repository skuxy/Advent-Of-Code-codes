import Data.List.Split

isABBA :: String -> Bool
isABBA lst@(a:b:c:d:xs) 
     | length lst > 4 = (a == d && b == c && a /= b) || isABBA (b:c:d:xs)
     | length lst == 4 = (a == d && b == c && a /= b)
     | otherwise = False

splitOnDms = splitOneOf "[]" 
checkLine [] = False
checkLine [x] =  isABBA x
checkLine (a:b:xs) = ((isABBA a) && (not $ isABBA b)) || checkLine xs  

main = do
        content <- readFile "test7.in"
	print $ length $ map (\x -> checkLine $ splitOnDms x) (lines content)
