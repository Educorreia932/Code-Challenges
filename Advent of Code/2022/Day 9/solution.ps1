function Clamp {
    param (
        $value,  
        $min,
        $max
    )

    if ($value -le $min){ 
        return $min 
    }
    
    elseif ($value -ge $max){ 
        return $max 
    }

    else { 
        return $value 
    }
}

function MoveTail {
    param (
        $head,
        $tail
    )
    
    $difference_x = $head[0] - $tail[0]
    $difference_y = $head[1] - $tail[1]

    if (([Math]::Abs($difference_x) -eq 2) -or ([Math]::Abs($difference_y) -eq 2)) {
        $offset_x = Clamp $difference_x -1 1
        $offset_y = Clamp $difference_y -1 1
        
        $tail = ($tail[0] + $offset_x), ($tail[1] + $offset_y)
    }

    $tail
}

function MoveHead {
    param (
        $head,
        $direction
    )

    switch ($direction) {
        'L' { $head[0]-- }
        'R' { $head[0]++ }
        'U' { $head[1]++ }
        'D' { $head[1]-- }
    }

    $head
}

function TailMotion {
    param(
        $head,
        $tail,
        $direction,
        $steps,
        $visited
    )

    for ($i = 0; $i -lt $steps; $i++) {
        $head = MoveHead $head $direction
        $tail = MoveTail $head $tail
        
        $visited.Add("$($tail[0]) $($tail[1])") > $null
    }

    $head, $tail
}

function PartOne {
    param (
        $motions
    )

    $head = 0, 0
    $tail = 0, 0
    $visited = New-Object System.Collections.Generic.HashSet[string]
    $visited.Add("$($tail[0]) $($tail[1])") > $null

    Foreach ($motion in $motions) {
        $direction, $steps = $motion.split(' ')
        $steps = [int]$steps

        $head, $tail = (TailMotion $head $tail $direction $steps $visited)
    }

    $visited.Count
}

function ReadInput {
    Get-Content -Path input.txt 
}

$motions = ReadInput

Write-Output (PartOne $motions)
