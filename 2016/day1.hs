--Haskell solution

parseDirection :: String -> (Int, Int, Char) -> (Int, Int, Char)
parseDirection (n:xs) (x,y,'N') 
    | n == 'R' = (x + read xs :: Int , y, 'E')
    | n == 'L' = (x - read xs :: Int , y, 'W')

parseDirection (n:xs) (x,y,'E') 
    | n == 'R' = (x, y - read xs :: Int , 'S')
    | n == 'L' = (x, y + read xs :: Int , 'N')

parseDirection (n:xs) (x,y,'S') = parseDirection (n:'-':xs) (x,y,'N')
parseDirection (n:xs) (x,y,'W') = parseDirection (n:'-':xs) (x,y,'E')
