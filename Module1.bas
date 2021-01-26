Attribute VB_Name = "Module1"
Sub setEverything()
    'Dim cols As Integer
    'Dim rows As Integer
    Dim s1 As Worksheet
    Dim lr As Integer
    
    lr = Range("A1", Range("A1").End(xlDown)).Rows.Count
    Set s1 = Worksheets("Sheet1")
    Set hr = Worksheets("Sheet1").Range("A1", Range("A1").End(xlToRight))
    
    'Set iR = Worksheets("Sheet1").Range("A2", Range("A2").End(xlDown))
    'cols = Worksheets("Sheet1").Range("A1", Range("A1").End(xlToRight)).Columns.Count
    'rows = Worksheets("Sheet1").Range("A2", Range("A2").End(xlDown)).rows.Count
    'Worksheets("Sheet1").Activate
    'Worksheets("Sheet1").rows(1).Select
    'Range("K2", Range("K" & rows.Count).End(xlUp)).Select
    'With Worksheets("Sheet1").Range("K2", Range("K2").End(xlDown))
    
    With s1.Range(Range("A" & lr), hr)
    .Borders(xlInsideHorizontal).LineStyle = xlContinuous
    .Borders(xlEdgeLeft).LineStyle = xlContinuous
    .Borders(xlEdgeRight).LineStyle = xlContinuous
    .Borders(xlEdgeBottom).LineStyle = xlContinuous
    End With
    
    hr.HorizontalAlignment = xlCenter
    hr.AutoFilter
    
    With ActiveWindow
        .SplitColumn = 1
        .SplitRow = 1
    End With
    ActiveWindow.FreezePanes = True

    Worksheets("Sheet1").Columns("A").ColumnWidth = 6

    Worksheets("Sheet1").Columns("B").Hidden = True
    Worksheets("Sheet1").Columns("C").Hidden = True
    Worksheets("Sheet1").Columns("D").Hidden = True
    Worksheets("Sheet1").Columns("E").Hidden = True
    Worksheets("Sheet1").Columns("F").Hidden = True
    Worksheets("Sheet1").Columns("G").Hidden = True

    Worksheets("Sheet1").Columns("H").ColumnWidth = 10
    With s1.Range("H2", Range("H" & lr))
    .HorizontalAlignment = xlLeft
    .VerticalAlignment = xlVAlignTop
    End With

    Worksheets("Sheet1").Columns("I").ColumnWidth = 12
    With s1.Range("I2", Range("I" & lr))
    .VerticalAlignment = xlVAlignCenter
    .HorizontalAlignment = xlLeft
    End With

    Worksheets("Sheet1").Columns("J").ColumnWidth = 50
    With s1.Range("J2", Range("J" & lr))
    .HorizontalAlignment = xlLeft
    .VerticalAlignment = xlVAlignTop
    .WrapText = True
    End With

    Worksheets("Sheet1").Columns("K").ColumnWidth = 13
    
    With s1.Range("K2", Range("K" & lr))
    .VerticalAlignment = xlVAlignCenter
    .HorizontalAlignment = xlLeft
    End With

    Worksheets("Sheet1").Columns("L").Hidden = True

    Worksheets("Sheet1").Columns("M").ColumnWidth = 9
    With s1.Range("M2", Range("M" & lr))
    .VerticalAlignment = xlVAlignTop
    .HorizontalAlignment = xlLeft
    End With

    Worksheets("Sheet1").Columns("N").Hidden = True

    Worksheets("Sheet1").Columns("O").ColumnWidth = 25
    With s1.Range("O2", Range("O" & lr))
    .VerticalAlignment = xlVAlignTop
    .HorizontalAlignment = xlLeft
    End With

    Worksheets("Sheet1").Columns("P").ColumnWidth = 20
    With s1.Range("P2", Range("P" & lr))
    .VerticalAlignment = xlVAlignTop
    .HorizontalAlignment = xlLeft
    End With

    Worksheets("Sheet1").Columns("Q").ColumnWidth = 115
    With s1.Range("Q2", Range("Q" & lr))
    .VerticalAlignment = xlVAlignTop
    .HorizontalAlignment = xlLeft
    End With
    
    Call AutoFitAbs

    Call setText
End Sub
Sub setText()
    Dim x As Integer
    Dim NumRows As Integer
    Dim NumCols As Integer
    ' Set numrows = number of rows of data.
    NumRows = Range("A1", Range("A1").End(xlDown)).Rows.Count
    NumCols = Range("A1", Range("A1").End(xlToRight)).Columns.Count
    ' Select cell a1.
    Range("A2").Select
    ' Establish "For" loop to loop "numrows" number of times.
DoTheRows:
    For x = 1 To NumRows
        ' Insert your code here.
        'Application.SendKeys "{F2}"
        'Application.SendKeys "~"
        ActiveCell.Select
        If InStr(ActiveCell, vbCr) Then
            ActiveCell = WorksheetFunction.Substitute(ActiveCell, vbCr, vbLf)
        End If
        
        ActiveCell.Offset(1, 0).Select
        If ActiveCell.row = NumRows + 1 Then
            If ActiveCell.Column = NumCols - 1 Then
                GoTo EndIt
            Else
                ActiveCell.Offset(-NumRows, 1).Select
                GoTo DoTheRows
            End If
        End If
    Next
EndIt:
    Range("A2").Select
    End Sub
Sub AutoFitAbs()
    Dim row As Range, MyRows As Range, lastRow As Integer
    Dim ws As Worksheet

    Set MyRows = ActiveWorkbook.Worksheets("Sheet1").Range("Q2", Range("Q2").End(xlDown))

    Set ws = ActiveWorkbook.Worksheets.Add
    ws.Visible = xlSheetHidden

    Application.DisplayAlerts = False

    For Each row In MyRows
       ' Insert your code here.
        ws.Range("A1").Value = row.Value
        ws.Range("A1").ColumnWidth = 115
        ws.Range("A1").WrapText = True

        row.EntireRow.RowHeight = ws.Rows(1).RowHeight
    Next row
    MyRows.WrapText = True
  ws.Delete

  Application.DisplayAlerts = True

End Sub
















