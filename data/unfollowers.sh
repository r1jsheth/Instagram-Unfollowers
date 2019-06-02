#!/bin/bash
echo "Enter previous filename:"
read prevFileName
echo "Enter new filename:"
read newFileName

# Following line of code finds followers gained
# Output stored in newFollowers file, change according to your need
fgrep -vxf $prevFileName $newFileName >> newFollowers
echo "New Followers:"
cat newFollowers

# Following line of code finds all the followers lost
# Output stored in unfollowers file, change according to your need
fgrep -vxf $newFileName $prevFileName >> unfollowers
echo "Unfollowers:"
cat unfollowers