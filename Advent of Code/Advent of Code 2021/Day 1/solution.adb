with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

procedure Main is
	File     : File_Type;
	Counter  : Natural := 0;
	Previous : Integer := 2147483647;
begin
	Open (File, In_File, "input.txt");

	while not End_Of_File (File) loop
		declare
			N : Integer := Integer'Value (Get_Line (File));
		begin
			if N > Previous then
				Counter := Counter + 1;
			end if;

			Previous := N;
		end;
	end loop;

	Put_Line(Counter'Image);

	Close (File);
end Main;