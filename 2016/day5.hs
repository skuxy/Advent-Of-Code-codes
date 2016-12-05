import Data.List
import Data.String
import Data.Hash.MD5

input = "ffykfhsq"

concatInteger input integer = input ++ show integer

init5Zeroes string = "00000" == take 5 string

main = do
	print $ md5s $ input 
	
