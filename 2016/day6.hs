import Data.List

type Triple  = (Char, Int, Int)--Character on index for n times

elemOccurs :: [Triple] -> (Char, Int) -> Bool
elemOccurs [] _ = False
elemOccurs ((a,b,c):xs) (x,y) = if (a == x) && (b == y) then  True else elemOccurs xs (x,y)

incrElem :: [Triple] -> (Char, Int) -> [Triple]
incrElem ((a,b,c):xs) (x,y) = if (a==x) && (b==y) then (a,b,c+1) : xs else (a,b,c) : incrElem xs (x,y)

addToOccurs :: [Triple] -> (Char, Int) -> [Triple]
addToOccurs elems (x,y)  = if not $ elemOccurs elems (x,y) then elems ++ [(x,y,1)] else incrElem elems (x,y)

countElems :: [Triple] -> String -> Int -> [Triple]
countElems list "" _= list
countElems list (x:xs) n =  countElems (addToOccurs list (x,n)) xs (n+1)
  
parseLines :: [String] -> [Triple] -> [Triple]
parseLines [] counts = counts
parseLines (x:xs) counts = parseLines xs (countElems counts x 0) 

getIndex n  = filter (\x -> snd x == n) 

compareTriples :: (Ord a, Ord b, Ord c) => (a,b,c) -> (a,b,c) -> Ordering
compareTriples (a,b,c) (d,e,f) =
    case compare f c of
        ne -> ne

compareTriples' :: (Ord a, Ord b, Ord c) => (a,b,c) -> (a,b,c) -> Ordering
compareTriples' (a,b,c) (d,e,f) =
    case compare c f of
        ne -> ne

getMaxIndexes [] maxes _ = maxes
getMaxIndexes elems maxes n = getMaxIndexes filterOld (maxes ++ [findMax]) (n+1)
    where filterOld = filter (\(a,b,c) -> b > n) elems 
          findMax =  head $ sortBy compareTriples (filter (\(a,b,c) -> b == n) elems)

getMinIndexes [] mins _ = mins
getMinIndexes elems mins n = getMinIndexes filterOld (mins ++ [findMin]) (n+1)
    where filterOld = filter (\(a,b,c) -> b > n) elems 
          findMin =  head $ sortBy compareTriples' (filter (\(a,b,c) -> b == n) elems)
main = do
        content <- readFile "day6.in"
        print $ map (\(a,_,_) -> a) $ getMaxIndexes (parseLines ( lines content ) []) [] 0 
        print $ map (\(a,_,_) -> a) $ getMinIndexes (parseLines ( lines content ) []) [] 0 
	
