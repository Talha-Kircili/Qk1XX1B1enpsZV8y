# Methodology

## 1. Phase: Investigating the [partners page](https://security-challenge.bmw-carit.de/fabulousmobility/partners)

### Partner authentication service: 

- challenge-response authentication with rsa keys

- obtaining short-lived api token after successful login

### Technical Protocol Information:

<img src=mobility-auth-flow.png>   

- text-based authentication server at **security-challenge.bmw-carit.de:21042**

## 2. Phase: Exploring the authentication server 

- connecting to the server via telnet:  
  
  ```
  telnet security-challenge.bmw-carit.de 21042
  ```

- server responds with three certificates to choose from:  
  
  ``` 
  0) <Name(C=DE,ST=Baden-Wuerttemberg,L=Ulm,O=Fabulous Mobility\, Inc,OU=Marketing)>  
  1) <Name(C=DE,ST=Baden-Wuerttemberg,L=Ulm,O=Fabulous Mobilitc\, Inc,OU=Auth Services)>  
  2) <Name(C=DE,ST=Baden-Wuerttemberg,L=Ulm,O=Fabulous Mobility\, Inc,OU=Legacy Authentication)>  
  ```
- choosing a certificate from 0-2

- server responds with the corresponding [certificate](https://github.com/whIstl3bl0w3r/BMW_Puzzle_2/tree/main/certs) and a challenge  

## Background: Cube Root Attack  

When a small encryption **exponent e** is used and if the **message m** < **modulus n**/e:  
  
&nbsp; → the encryption is not effective since the ciphertext c is smaller than the modulus  
  
&nbsp; → adversary can calculate the cube root of the ciphertext to obtain the message

## 3. Phase: Inspecting the certificates  

- the certificates are pem-encoded X509 certificates

- copying the certificates into files similarly named to their OU

- extracting the [public key](https://github.com/whIstl3bl0w3r/BMW_Puzzle_2/tree/main/pubs) values:  
  ``` 
  openssl x509 -noout -in certs/<PEM> -modulus -text | \
  grep "Modulus=\|Exponent" | sed 's/^[ \t]*//' > pubs/<PUB>
  ```
- certificate 1\) and 2\) have the same **low exponent=3**:  
&nbsp; → vulnerable to Cube Root Attack?

## 4. Phase: Testing the certificates 1\) & 2\) for the Cube Root Attack 

### certificate 1\): message m < n/3
&nbsp; → vulnerable

### certificate 2\): modulus n/3 < message m
&nbsp; → not vulnerable

# Flag: Obtaining the api token  
``` python3 attacker.py ```  
  
Flag: **CIT-2cf2dc773a1be3b5a0d86a2914ee86b28a71975a113ca02bdf972a4bb28494cd**
