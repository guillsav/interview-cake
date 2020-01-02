# Product of All Other Numbers

You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function:

```
get_products_of_all_ints_except_at_index()
```

That takes a list of integers and returns a list of the products.

## **Example:**

```python
input: [1, 7, 3, 4]
```

Your function would return:

```python
output: [84, 12, 28, 21]
```

By calculating:

```python
[7 * 3 * 4, 1 * 3 * 4, 1 * 7 * 4, 1 * 7 * 3]
```

**Here's the catch: You can't use division in your solution!**
