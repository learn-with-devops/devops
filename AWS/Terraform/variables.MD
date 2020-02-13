
###  [1] Declare a String variable

variable "myvar" {
    type = string
    default = "hello anand"
}

        // Call the String Variable
        //    - terraform console
        //            - var.myvar  or "${var.myvar}"

###  [2] Declare a Map

variable "mymap" {
    type = map(string)
    default = {
            name = "anand"
            roll = 20
            dep = "cse"
    }
}

        // terraform console
        // - var.mymap or "${var.mymap}" or var.mymap["name"]

### [3] List Declaration

variable "mylist" {
    type = list
    default = [1,2,3]
}

        // terraform console
        // - var.mylist or var.mylist[0]

        // Print the element
            // element(var.mylist, 1)   //it will print the second element

        // Slice an element
            // slice(var.mylist, 0,2)   // It will print 0 , 1 
