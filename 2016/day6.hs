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

getMaxIndexes [] maxes _ = maxes
getMaxIndexes elems maxes n = getMaxIndexes (filter (\x -> snd x /= n) elems) (maxes : head $ sort $ map (\(a,b,c) ->c) $ filter (\x -> snd x == n) elems)


