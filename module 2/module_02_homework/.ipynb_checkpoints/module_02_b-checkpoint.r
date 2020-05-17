"
Class:       UCLA Intro to Data Science
Module:      02
Assignment:  Write a Python and R Program - part a (r)
Author:      Nathan Strong
Date:        April 19, 2020
"

BMI <- data.frame(
  gender = c("Male", "Male", "Female"),
  height = c(152, 171.5, 165),
  weight = c(81, 93, 78),
  Age = c(42, 38, 26)
)
print(BMI)

# Create and delete a hidden variable
.temp_var <- "I'll probably get deleted soon :("
print(ls(all.name = TRUE))
rm(.temp_var)
print(ls(all.name = TRUE))

# Create two vectors
vec_1 <- c(2, 5.5, 6)
vec_2 <- c(8, 3, 4)
vec_3 <- c(9, 2, 4)

# Add them together
print(vec_1 + vec_2)
# Test with a Relational Operator
print(vec_1 < vec_3)

# Make a sequence of numbers 2-8
numbers_2_to_8 <- 2:8
print(numbers_2_to_8)

# Make a function that takes a list and gets the square root for each value
get_square_roots <- function(list) {
  ret <- list()
  for (number in list) {
    ret <- append(ret, number * number)
  }
  return(ret)
}
# Run function
list_squared <- get_square_roots(numbers_2_to_8)
print(list_squared)


# Make a function with If/Else statement
check_for_string <- function(test, test_to_search_for) {
  if (grepl(test_to_search_for, test)) {
    return(paste(test_to_search_for, "is in", test))
  } else {
    return("Major Fail!")
  }
}
some_phrases <- list("cool beans", "coolio", "sweat deal", "Cool!")
test_to_search_for <- "cool"
for (phrase in some_phrases) {
  print(check_for_string(phrase, test_to_search_for))
}

