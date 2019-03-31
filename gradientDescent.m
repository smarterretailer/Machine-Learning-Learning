function [J] = gradientDescent((X, y)
  %WIP
  
  A = pinv(X'*X)*X'*y;
endfunction
  