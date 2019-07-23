for /l %x in (12000,1,12092) do copy *.jpg test\%x.jpg


for /l %x in (start, 每次加几 ,end) do copy *.jpg 目录\%x.jpg    （这个是复制命令）
for /l %x in (start, 每次加几 ,end) do ren *.jpg 目录\%x.jpg    （这个是重命名命令）