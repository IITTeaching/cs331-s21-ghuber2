import urllib
import requests

import urllib.request

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    words = book_to_words(book_url)
    return radixSort(words)


def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return [str(b)[2:-1] for b in bookascii.split()]


def counting_sort(arr,digit):
  """takes an array of words and a digit position returning a sorted list using a stable counting sorted"""
  output=len(arr)*[0]
  count=256*[0]

  for char_num in [ord(word[digit]) for word in arr]:
    count[char_num]+=1
  
  for char_num in range(1,256):
    count[char_num]+=count[char_num-1]
  
  for word in arr[::-1]:
     output[count[ord(word[digit])]-1]=word
     count[ord(word[digit])]-=1
  #print(output)
  return output

def radixSort(data):
  max_length = max([len(w) for w in data])
  for i in range(len(data)):
    data[i]+="\0"*(max_length-len(data[i]))
  for i in range(max_length-1,-1,-1):
   data = counting_sort(data,i)
  
  return [w.replace("\0","") for w in data]
