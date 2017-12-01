import Data.List.Split

initScreen = [['.' | _ <- [1..50]] | _ <- [1..6]]

initRect (x:y) = [['#' | _ <- [1..read [x] :: Int]] | _ <- [1..read y :: Int]]

main = do
    print "Oke"
