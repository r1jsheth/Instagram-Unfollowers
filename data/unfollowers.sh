#!/bin/bash
echo "Enter previous filename:"
read prevFileName
echo "Enter new filename:"
read newFileName
fgrep -vxf $prevFileName $newFileName >> newFollowers
fgrep -vxf $newFileName $prevFileName >> unfollowers