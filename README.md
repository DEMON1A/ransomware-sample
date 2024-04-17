# Demo Ransomware
A demostraion show-casing the actions of an actual ransomware, written in python

## Execution steps
1. List all the files inside the operation system ( windows in our case )
2. Create an encrypted copy of the files that can only be decrypted with a key we only know
3. Delete the orginal files in way that can't be recovered

## Attacker control 
In normal ransomware attacks, Attackers assign IDs to every victim where they can tell which key can decrypt their data, keeping the key to decrypt the data on the client side is really risky and would allow people analyzing the malware to just dumb the secret and decrypt the data

What I think we should do here is create an outside web server, generate random keys every time and assign an ID to every user, in the user README.md they should have an ID, once they contact us and send the payment, they should just provide the ID and we would send them the decrypting tool along with the key to decrypt their data.

## Encrypion Extension
`.enc` is a pretty lame extension, naming encrypted files `.rawrr` is pretty cool 