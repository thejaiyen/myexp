$fso = new-object -com Scripting.FileSystemObject
gci -Directory `
  | select @{l='Size'; e={$fso.GetFolder($_.FullName).Size}},FullName `
  | sort Size -Descending `
  | ft @{l='Size [MB]'; e={'{0:N2}    ' -f ($_.Size / 1MB)}},FullName