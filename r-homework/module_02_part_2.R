#A). Concatenate a set of integers, and strings and assign to a data frame
list_integers <- list(1, 2, 3, 4, 5)
list_strings <- list('a', 'b', 'c')
combined_dataframe <- data.frame(
  values = c(list_integers, list_strings)
)

#B). Take that list from A). and than separate out the integers and strings
list_of_integers_2 <- NULL
list_of_strings_2 <- NULL
for (value in combined_dataframe) {
  if (typeof(value) == 'character') {
    list_of_strings_2 <- append(list_of_strings_2, value)
  } else {
    list_of_integers_2 <- append(list_of_integers_2, value)
  }
}

#C). Create a function that computes the fibonacci sequence
count_max <- 10
val_1 <- 0
val_2 <- 1
count <- 2
if (count_max == 1) {
  print("Fibonacci sequence:")
  print(n1a)
} else {
  print("Fibonacci sequence:")
  print(val_1)
  print(val_2)
  while (count < count_max) {
    nth <- val_1 + val_2
    print(nth)
    val_1 <- val_2
    val_2 <- nth
    count <- count + 1
  }
}

#D). Sort a list of unsorted integers in a dataframe
some_numbers <- data.frame(
  numbers = c(5, 8, 1, 100, -2)
)
sort(some_numbers$numbers)


#E). Write an R while and for loop that match each other in number of iterations,
# printing out "Here I am"
iterate_amount <- 3
iterate_count <- 0

while(iterate_count < iterate_amount) {
  iterate_count <- iterate_count + 1
  print(iterate_count)
}

iterate_count <- 0

for (val in 1:iterate_amount) {
  iterate_count <- iterate_count + 1
  print(iterate_count)
}