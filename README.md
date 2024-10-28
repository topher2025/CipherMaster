# CipherMaster
 Encodes text in a variety of ciphers

 ## Caesar Cipher
  Encodes using caeser cipher
  The first argument, the shift number, is optional
  'e' for ENCODE and 'd' for DECODE is neccecary, and must be the last argument
  NOTE: With no shift input, the function will default to 3

  ---Example---
    
    $ caesar Have fun with this!! -4e
    lezi jyr amxl xlmw!!

 ## Clear
  Clears the console

 ## Help
  Gives a list of all commands
  When used with a specific comand it explains arguments for that function
  
  ---Example---
    
    $ help quit
    Quits the program

 ## Polibius
  Encodes using a 5x5 square
  The order input can take 1 (xy) or 0 (yx)
  NOTE: With no order input, the function defaults to xy (instead of yx)

  ---Example---
    
    $ polibius Have fun with this!! -0
    23 11 51 15  21 45 33  52 24 44 23  44 23 24 43 !!
    
 ## Quit
   Quits the program 