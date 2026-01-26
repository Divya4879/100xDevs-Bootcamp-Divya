i =  int(input())

# for x in range(1,i+1):
#     print("* "*x)
    
# for x in range(1,i):
#     print("* "*(i-x))
    
    
'''

Sample Input
5

Your Output
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''

# for x in range(0,i):
#     for y in range(0,i):
#         if y==0 or x==y:
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()
    
# for x in range(0,i-1):
#     for y in range(0,i-1):
#         if y==0 or y==i-2-x:
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()
    
'''

Sample Input
5

Your Output
*     
* *    
*  *   
*   *  
*    * 
*   * 
*  *  
* *   
*    

'''

# for x in range(i):
#     print(" "*(i-x-1),"*"*(x+1))
    
    
'''

Sample Input
5

Your Output
     *
    **
   ***
  ****
 *****
 
'''

# for x in range(i):
#     print(" "*(i-x-1),"* "*(x+1))
    
    
'''

Sample Input
5

Your Output
     *      
    * *     
   * * *    
  * * * *   
 * * * * *  
 
'''

# for x in range(i):
#     for y in range(i*2):
#         if (x==i-1 and y<=i and y<=x):
#             print("* ",end="",sep="")
#         elif (x==0 and y==i-1) or x+y==i-1 or (y-x==i-1 and y!=2*x):
#             print("*",end="",sep="")
#         else:
#             print(" ",end="",sep="")
#     print()
    
'''

Sample Input
5

Your Output

    *     
   * *    
  *   *   
 *     *  
* * * * *      
 
'''
 
# for x in range(i):
#     print(" "*(x), "* "*(i-x)," "*(x))
    
    
'''

Sample Input
5

Your Output
    
 * * * * *  
  * * * *   
   * * *    
    * *     
     *     
'''

# for x in range(i-1,0,-1):
#     print(" "*(x), "* "*(i-x)," "*(x))
# for x in range(i):
#     print(" "*(x), "* "*(i-x)," "*(x))
    
'''

Sample Input
10

Your Output
          *           
         * *          
        * * *         
       * * * *        
      * * * * *       
     * * * * * *      
    * * * * * * *     
   * * * * * * * *    
  * * * * * * * * *   
 * * * * * * * * * *  
  * * * * * * * * *   
   * * * * * * * *    
    * * * * * * *     
     * * * * * *      
      * * * * *       
       * * * *        
        * * *         
         * *          
          *  

          
'''


# for x in range(i):
#     for y in range(2*i):
#         if (y+x==i-1) or (y-x==i and y!=i):
#             print("*",end="",sep="")
#         else:
#             print(" ",end="",sep="")
#     print()
    
# for x in range(i-1):
#     for y in range(2*i):
#         if (y-x==1) or (x+y==2*i-2 and x!=i-2):
#             print("*",end="",sep="")
#         else:
#             print(" ",end="",sep="")
#     print()

    
    
'''

Sample Input
10

Your Output
         *          
        *  *        
       *    *       
      *      *      
     *        *     
    *          *    
   *            *   
  *              *  
 *                * 
*                  *
 *                * 
  *              *  
   *            *   
    *          *    
     *        *     
      *      *      
       *    *       
        *  *        
         *          
'''

# for x in range(i):
#     print("* "*(x+1) + " "*(4*(i-x-1))+ "* "*(x+1))
    
'''

Sample Input
10

Your Output
*                                     * 
* *                                 * * 
* * *                             * * * 
* * * *                         * * * * 
* * * * *                     * * * * * 
* * * * * *                 * * * * * * 
* * * * * * *             * * * * * * * 
* * * * * * * *         * * * * * * * * 
* * * * * * * * *     * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 

'''


# for x in range(i):
#     print("* "*(x+1) + " "*(4*(i-x-1))+ "* "*(x+1))
    
# for x in range(i-1):
#     print("* "*(i-x-1) + " "*(4*(x+1))+ "* "*(i-x-1))
    
'''

Sample Input
10

Your Output
*                                     * 
* *                                 * * 
* * *                             * * * 
* * * *                         * * * * 
* * * * *                     * * * * * 
* * * * * *                 * * * * * * 
* * * * * * *             * * * * * * * 
* * * * * * * *         * * * * * * * * 
* * * * * * * * *     * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * *     * * * * * * * * * 
* * * * * * * *         * * * * * * * * 
* * * * * * *             * * * * * * * 
* * * * * *                 * * * * * * 
* * * * *                     * * * * * 
* * * *                         * * * * 
* * *                             * * * 
* *                                 * * 
*                                     * 

'''

for x in range(i):
  print("* "*(i-x) + " "*(4*(x))+ "* "*(i-x))
  
for x in range(1,i):
    print("* "*(x+1) + " "*(4*(i-x-1))+ "* "*(x+1))
    
    
'''

Sample Input
10

Your Output
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * *     * * * * * * * * * 
* * * * * * * *         * * * * * * * * 
* * * * * * *             * * * * * * * 
* * * * * *                 * * * * * * 
* * * * *                     * * * * * 
* * * *                         * * * * 
* * *                             * * * 
* *                                 * * 
*                                     * 
* *                                 * * 
* * *                             * * * 
* * * *                         * * * * 
* * * * *                     * * * * * 
* * * * * *                 * * * * * * 
* * * * * * *             * * * * * * * 
* * * * * * * *         * * * * * * * * 
* * * * * * * * *     * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 

'''