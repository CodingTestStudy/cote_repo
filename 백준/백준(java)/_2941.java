package practice;

import java.util.Scanner;

public class _2941 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		int answer = 0;
		
		int index = 0;
		while(index != str.length()) {
			//마지막 문자인 경우, 일반 알파벳 취급 
			if(index == str.length() - 1) {
				answer++;
				break;
			}
			
			char ch = str.charAt(index);
			//c로 시작하는 경우 
			if(ch == 'c') {
				//다음 문자가 - or = 인 경우 
				if(str.charAt(index + 1) == '=' || str.charAt(index + 1) == '-') {
					index += 2;					
				}
				//일반 알파벳인 경우 
				else {
					index += 1;
				}
			//d로 시작하는 경우 
			}else if(ch == 'd') {
				//d 다음 -가 오는 경우 
				if(str.charAt(index + 1) == '-') {
					index += 2;
				}
				//d 다음 z가 오는 경우 
				else if(str.charAt(index + 1) == 'z') {
					//3글자가 될 수 없는 경우, 일반 알파벳 취급 
					if((index + 2) == str.length()) {
						index += 1;
					}
					//3글자가 가능한 경우 
					else {
						//'dz='인 경우 
						if(str.charAt(index + 2) == '=') {
							index += 3;
						}
						//그 외의 경우, 일반 알파벳 취급
						else {
							index += 1;
						}
					}
				}
				//일반 알파벳 취급 
				else {
					index += 1;
				}
			}else if(ch == 'l') {
				if(str.charAt(index + 1) == 'j') {
					index += 2;
				}else {
					index += 1;
				}
			}else if(ch == 'n') {
				if(str.charAt(index + 1) == 'j') {
					index += 2;
				}else {
					index += 1;
				}
			}else if(ch == 's') {
				if(str.charAt(index + 1) == '=') {
					index += 2;
				}else {
					index += 1;
				}
			}else if(ch == 'z') {
				if(str.charAt(index + 1) == '=') {
					index += 2;
				}else {
					index += 1;
				}
			}else {
				index += 1;
			}
			answer += 1;
		}
		System.out.println(answer);
	}

}
