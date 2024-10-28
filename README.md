# CipherMaster
 Encodes text in a variety of ciphers

 ## Help
  Gives a list of all commands. vWhen used with a specific comand it explains arguments for that function
  
  ---Example---
    
    $ help quit
    Quits the program

 ## Caesar Cipher
  Encodes using [caeser cipher](https://en.wikipedia.org/wiki/Caesar_cipher). The first argument, the shift number, is optional
  'e' for ENCODE and 'd' for DECODE is neccecary, and must be the last argument
  NOTE: With no shift input, the function will default to 3

  ---Example---
    
    $ caesar Have fun with this!! -4e
    lezi jyr amxl xlmw!!

 ## Polybius
  Encodes using a [polyius cipher](https://en.wikipedia.org/wiki/Polybius_square),a 5x5 square cipher. The order input can take 1 (xy) or 0 (yx)
  NOTE: With no order input, the function defaults to xy (instead of yx)

  ---Example---
    
    $ polibius Have fun with this!! -0
    23 11 51 15  21 45 33  52 24 44 23  44 23 24 43 !!
    
  ## Clear
   Clears the console
 ## Quit
   Quits the program 