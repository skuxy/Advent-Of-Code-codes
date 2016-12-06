import Data.List


type Occurs = [(Char, Int, Int)]--Character on index for n times

elemOccurs [] _ = False
elemOccurs ((a,b,c):xs) (x,y) = if (a == x) && (b == y) then  True else elemOccurs xs (x,y)

incrElem ((a,b,c):xs) (x,y) = if (a==x) && (b==y) then (a,b,c+1) : xs else (a,b,c) : incrElem xs (x,y)

addToOccurs elems (x,y)  = if not $ elemOccurs elems (x,y) then elems ++ [(x,y,1)] else incrElem elems (x,y)

countElems list "" _= list
countElems list (x:xs) n =  countElems (addToOccurs list (x,n)) xs n+1
  
