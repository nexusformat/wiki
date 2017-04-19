#! /bin/sh

newdate=$1

echo $newdate | grep 20..[01].[0123]. > /dev/null || (echo no proper new date given as argument >&2 ; exit 1)

# Wednesday, 8th March, 16:30 Central European Summer Time (Copenhagen)
ndatestr=`date -jf "%Y%m%d" $newdate "+%A, %e %B, 16:30 %Z (%z)"`

nyear=`date -jf "%Y%m%d" $newdate +%Y`
nmonth=`date -jf "%Y%m%d" $newdate +%m`
nmonthstr=`date -jf "%Y%m%d" $newdate +%B`

# copy old one
oldone=`ls Telco_*.md | tail -1 | sed -e s/Telco_// -e s/.md//`

oyear=`date -jf "%Y%m%d" $oldone +%Y`
omonth=`date -jf "%Y%m%d" $oldone +%m`

cat > Telco_$newdate.md <<EOF
---
title: Telco $newdate
permalink: Telco_$newdate.html
layout: wiki
---

Date
----

$ndatestr

EOF

sed -n '/end of autogeneration/,$p' < Telco_$oldone.md >> Telco_$newdate.md

if [ $nyear != $oyear ] ; then
ed Teleconferences.md <<EOF
/### $oyear/
i
### $nyear

.
w
q
EOF
fi

if [ $nmonth != $omonth ] ; then
ed Teleconferences.md <<EOF
/### $nyear/
a

#### $nmonthstr

.
w
q
EOF
fi

ed Teleconferences.md <<EOF
/#### $nmonthstr
a

[Telco $newdate](Telco_$newdate.html "wikilink") $ndatestr
.
w
q
EOF

cat >> Telco_$oldone.md <<EOF

### Next Meeting
[Telco $newdate](Telco_$newdate.html)

EOF

vi Telco_$newdate.md

# add to git index
git add Telco_$newdate.md Teleconferences.md Telco_$oldone.md

cat <<EOF

################################################
################################################
 Don't forget to send out the calendar invite!
################################################
################################################

EOF
