# How to use the mmo module

In this folder (or the folder the mmo.py file is located), create a new python file, or open the command line.

## Setup
To import the module, just do

```python
import mmo
```

To import the post, you can either paste into the function itself, or load a file (which I recommend)

```python
f = open('mmo leaderboard.txt','r',encoding='utf8')
post = f.read()
f.close()
mmo.getLeaderboards(post)
```

Replace `mmo leaderboard.txt` with the file with the post in it.

To import a post without a file, just put the text inside the `mmo.getLeaderboards()` function.

# Usage

To get started, here's the category names I used

| actual name | used name  |
|-------------|------------|
|Any%         |any         |
|Crouchless   |crouchless  |
|Refresh%     |refresh     |
|Minimum Jumps|jumps       |
|Test%        |test        |

If you want to use the actual names, then just put this in for the name
```python
mmo.categories['Any%']
```
Change `'Any%'` to whatever categoy you want. Note: they are case sensative.

## Getting leaderboard info

To get a leaderboard, just use this

```python
mmo.leaderboard[category]
```

Example

```python
mmo.leaderboard['any']
```

To get a users info just do this

```python
mmo.leaderboard[category][user]
```

Example:

```python
mmo.leaderboard['any']['ego-lay_atman-bay']
```

The result is

```python
{'time': "1'02.1"}
```
In the `'jumps'` category, it'll be
```
{'time': "5'55.0", 'jumps': '12'}
```

To get the individual value, just do this

```python
mmo.leaderboard[category][user][info]
```

Example:

```python
mmo.leaderboard['jumps']['IceBryker']['time']
```
will return
```python
"5'55.0"
```

## Adding/update a run

To add/update a run, just use this function.

```python
mmo.addTime(category,user,time,(jumps))
```

You only need the `jumps` argument if the category is `'jumps'`

Example:
```python
mmo.addTime('any','ego-lay_atman-bay',"1'03.2")
```

## Deleting a run

To delete a run, just use this

```python
delTime(user)
```

The `user` argument is case sensative so you need to type in the user with the correct case

Example:
```python
delTime('ego-lay_atman-bay')
```

## Exporting

To export the post, just use this function

```
mmo.export()
```

This function will create a new file called `'mmo leaderboard (current date)'`, for example, `'mmo leaderboard 02-05-22'`

## Sorting a categoy

You shouldn't need to do this, since this is already done when the `addTime()` function is ran

```python
mmo.sortCategory(category)
```

This returns the sorted category, it does not update the actual leaderboard. To update the leaderboard, just do

```python
mmo.leaderboard[category] = mmo.sortCategory(category)
```
Example:
```python
mmo.leaderboard['any'] = mmo.sortCategory('any')
```