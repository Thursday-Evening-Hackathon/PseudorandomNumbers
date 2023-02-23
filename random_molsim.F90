module Random_Module
   integer, parameter :: k4b=selected_int_kind(9) ! = 4 on intel fortran and gfortran
   real(8) :: am
   integer(k4b) :: ix=-1,iy=-1
   integer(k4b) :: ix2=-1,iy2=-1
   integer(k4b) :: ix3=-1,iy3=-1
   integer(k4b) :: ix4=-1,iy4=-1
end module Random_Module

function Random(idum)
   use Random_Module
   implicit none
   integer(k4b), intent(inout) :: idum
   real(8) :: Random
   integer(k4b), parameter :: ia=16807,im=2147483647,iq=127773,ir=2836
   integer(k4b)   :: k
   if (idum <= 0 .or. iy < 0) then           !initialize.
      am=nearest(1.0,-1.0)/im
      iy=ior(ieor(888889999,abs(idum)),1)
      ix=ieor(777755555,abs(idum))
      idum=abs(idum)+1                          !set idum positive.
   end if
   ix=ieor(ix,ishft(ix,13))                  !marsaglia shift sequence with period 2^32 − 1.
   ix=ieor(ix,ishft(ix,-17))
   ix=ieor(ix,ishft(ix,5))
   k=iy/iq                                   !park-miller sequence by schrage’s method, period 2^31 − 2.
   iy=ia*(iy-k*iq)-ir*k
   if (iy < 0) iy=iy+im
   Random=am*ior(iand(im,ieor(ix,iy)),1)     !combine the two generators with masking to ensure nonzero value.
end function Random
