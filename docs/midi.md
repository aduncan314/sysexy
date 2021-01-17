# About Midi #

## Overview ##

### Messages ###
Every midi message is one byte framed by a start bit and an end bit. Since a byte is 8 bits, every
midi message is 10 bits. The first bit determines if the message is a status message or a data
message.

## Resources ##
- [Midi Association Spec](https://www.midi.org/specifications)
- [Midi Association Message list](
https://www.midi.org/specifications-old/item/table-2-expanded-messages-list-status-bytes)
  
- [DSI PEK Manual]( 
https://www.davesmithinstruments.com/downloads/poly_evolver_key/doc/Poly_Evo_Key_Manual_1.4.pdf)
  
- [Possible Ideas](https://forums.cockos.com/showthread.php?t=142527)