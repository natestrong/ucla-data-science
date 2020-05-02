someVariable <- 15
print(someVariable)

someFunction <- function() {
  #this variable is LOCAL only
  someOtherVariable <- "foobar"
  print(someOtherVariable)
}

someFunction <- function(arg1, arg2) {
  #this variable is LOCAL only
  result <- arg1*arg2

}
  
someOtherVariable <- someOtherFunction(4,4)
print(someOtherVariable)


compareAndLoop <- function() {
  a <- 10
  b <- 100

  if(a < b){
    result<- "a is less than b"
  }
  else if (a == b){
    result<- "a is same as b"
  }
  else{
    result<- "a is greater than b"
  }
  print(result)
 
  x <- 1

  while (x < 5){ 
     x <- x *5
     print(x)
   }
}
     
  
   