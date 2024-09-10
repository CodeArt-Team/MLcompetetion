//
//  SettingView.swift
//  HaruSijak
//
//  Created by 신나라 on 6/11/24.
//
// MARK: -- Description
/*
    Description : HaruSijack App 개발 setting page
    Date : 2024.6.11
    Author : snr
    Detail :
    Updates :
        * 2024.06.11 by snr : Add tabbar icon for settingPage
        * 2024.06.12 by snr : 시간대 변경 sheet 생성
        * 2024.06.13 by snr : 시간설정 추가 및 수정기능 완료
                              시간 선택 picker를 TimeSettingView로 view로 생성함 -> 다른페이지에서도 사용하기 위해
 
        * 2024.06.17 by snr : 시간설정 + 출발역 지정 기능 추가하기
        * 2024.06.27 by pdg : 시간 설정 칸 이랑 버전 정보랑 구분이 안감. -> 시간 설정은 버튼화 했으면 좋겠음.
        * 2024.08.19 by snr : 역, 호선, 시간 변경 시 바로 update되어 조회되도록 수정
        * 2024.09.09 by snr : 역, 시간 정보를 설정했을 때만 상세정보가 보이도록 수정
        * 2024.09.10 by snr : 뒤로가기 버튼 커스터마이징.
 
 */
import SwiftUI
struct SettingView: View {
    @State var isShowSheet: Bool = false        // 시간 변경 sheet alert
    @State var isStationSheet: Bool = false     // 역 변경 sheet alert
    let dbModel = TimeSettingDB()               // 시간 설정 vm instance 생성
    @State var infoList: [Time] = []            // 조회된 시간정보 담을 리스트
    
    @State var stationName: String =  TimeSettingDB().queryDB().first!.station
    @State var line: Int = TimeSettingDB().queryDB().first!.line
    @State var time: Int = TimeSettingDB().queryDB().first!.time
    
    @Environment(\.dismiss) var dismiss;
    

    var body: some View {
            VStack(content: {
                
                // ********* 백업 *********
//                HStack(content: {
//                    Button(action: {
//                        isShowSheet = true
//                    }, label: {
//                        Image(systemName: "slider.horizontal.2.square")
//                            .font(.system(size: 25))
//                            .padding()
//
//                            Text("출발역 지정하기")
//
//                            // line이 124가 아닐 때만, 즉 시간과 역설정 되었을 때만 해당 정보가 출력되도록 함.
//                            if line != 124{
//                                Text("(\(stationName)역 [\(line)호선],  \(time)시)") // 저장되어있는 설정시간 보여주기
//                                    .font(.custom("Ownglyph_noocar-Rg", size: 18))
//                                    .foregroundStyle(.gray)
//                                    .padding(.top, 3)
//                            }
//                    })
//
//                })
//                .frame(maxWidth: /*@START_MENU_TOKEN@*/.infinity/*@END_MENU_TOKEN@*/, alignment: .leading)
//                .padding(.leading, 20)
//                .onTapGesture {
//                    isShowSheet = true
//                }
                
            // ********* 출근 역 설정버튼 start *********
                HStack(content: {
                    Button(action: {
                        isStationSheet = true
                    }, label: {
                        Image(systemName: "train.side.rear.car")
                            .font(.system(size: 25))
                            .padding()
                        
                        Text("출발역")
                            .padding(.trailing, 20)
                        
                        // line이 124가 아닐 때만, 즉 시간과 역설정 되었을 때만 해당 정보가 출력되도록 함.
                        if line != 124{
                            Text("\(stationName)역 [\(line)호선]") // 저장되어있는 설정시간 보여주기
                                .font(.custom("Ownglyph_noocar-Rg", size: 20))
                                .foregroundStyle(.gray)
                                .padding(.top, 3)
                        }
                    })
                    
                })
                .frame(maxWidth: /*@START_MENU_TOKEN@*/.infinity/*@END_MENU_TOKEN@*/, alignment: .leading)
                .padding(.leading, 20)
                .onTapGesture {
                    isStationSheet = true
                }
                
                
            
                // ********* 시간대 설정버튼 start *********
                HStack(content: {
                    Button(action: {
                        isShowSheet = true
                    }, label: {
                        Image(systemName: "clock")
                            .font(.system(size: 25))
                            .padding()
                        
                            Text("출발시간")
                                .padding(.trailing, 15)
                            
                            // line이 124가 아닐 때만, 즉 시간과 역설정 되었을 때만 해당 정보가 출력되도록 함.
                            if line != 124{
                                Text("\(time)시") // 저장되어있는 설정시간 보여주기
                                    .font(.custom("Ownglyph_noocar-Rg", size: 20))
                                    .foregroundStyle(.gray)
                                    .padding(.top, 3)
                            }
                    })
                    
                })
                .frame(maxWidth: /*@START_MENU_TOKEN@*/.infinity/*@END_MENU_TOKEN@*/, alignment: .leading)
                .padding(.leading, 20)
                .onTapGesture {
                    isShowSheet = true
                }
                
                
                
                
                // ********* 버전정보 start  *********
                HStack(content: {
                    Image(systemName: "v.square")
                        .font(.system(size: 25))
                        .padding()
                    
                    Text("버전정보 : v.1.0.0")
                })
                .frame(maxWidth: /*@START_MENU_TOKEN@*/.infinity/*@END_MENU_TOKEN@*/, alignment: .leading)
                .padding(.leading, 20)
                
                
                Spacer()
                
            })//Vstack
            .padding(.top, 30)
            .font(.custom("Ownglyph_noocar-Rg", size: 20))
            .sheet(isPresented: $isShowSheet, content: {
                TimeSettingView(titleName: "출발시간 설정", stationValue: $stationName, lineValue: $line, timeValue: $time)
                    .onDisappear{
//                        fetchTasksForSelectedDate()
                        print("Updated TimeValue: \(stationName), line: \(line), time: \(time)")
                    }
                    .presentationDragIndicator(.visible)
                    .presentationDetents([.medium])
            })// 시간 설정 sheet
            .sheet(isPresented: $isStationSheet, content: {
                StationSettingView(titleName: "출발역 설정", stationValue: $stationName, lineValue: $line, timeValue: $time)
                    .onDisappear{
                        fetchTasksForSelectedDate()
                      print("Updated stationValue: \(stationName), line: \(line), time: \(time)")
                    }
                    .presentationDragIndicator(.visible)
                    .presentationDetents([.medium])
            }) // 역 설정 sheet
            .toolbar {
                ToolbarItem(placement: .principal) {
                    Text("설정")
                        .font(.custom("Tenada", size: 30))
                }
                
                ToolbarItem(placement: .topBarLeading) {
                    Button(action: {
                        dismiss() //뒤로가기 함수
                    }, label: {
                        Image(systemName: "house.fill")
                            .imageScale(.large)
                            .foregroundColor(.primary)
                    })
                }
            }
            .navigationBarBackButtonHidden(true) //Back 버튼 숨기기
        }
    
    
    /* MARK: 설정 값 reload 함수*/
    func fetchTasksForSelectedDate(){
        guard let result = dbModel.queryDB().first else { return }
        print("line : ", result.line)
        print("stationName : ", result.station)
        print("time : ", result.time)
        
        stationName = result.station
        time = result.time
        line = result.line
    }
}

#Preview {
    SettingView(stationName: "가디", line: 1, time: 1)
}
