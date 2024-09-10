//
//  TimeSettingView.swift
//  HaruSijak
//
//  Created by 신나라 on 6/13/24.
/*
    Description : HaruSijack App 개발 setting page
    Date : 2024.6.13
    Author : snr
    Detail :
    Updates :
        * 2024.07.05 by snr : 호선과 역명 설정되도록 수정
        * 2024.09.09 by snr : 
            1. 제목, 버튼 글꼴 수정
            2. SettingView에서 넘어오는 Line 값이 임의로 설정한 124일 경우, 1호선부터 조회되도록 selectedLine = 0 처리
        * 2024.09.10 by snr : 시간, 역 설정 화면 분리
 */

import SwiftUI

struct TimeSettingView: View {
    
//    @State var isShowSheet: Bool = false    // 시간 변경 sheet alert
    let timeList = [Int](5..<25)            // 5~24까지 리스트
    let line23 = SubwayList().totalStation
    
    let dbModel = TimeSettingDB()           // 시간 설정 vm instance 생성
    @State var infoList: [Time] = []        // 조회된 시간정보 담을 리스트
    @Environment(\.dismiss) var dismiss         // 화면 이동을 위한 변수
    @State var alertType: SettingAlertType?        // 추가, 수정 alert
    @State var titleName : String
    
    @State var selectedTime = 0             // picker뷰 선택 value
    @State var selectedStation = 0          // station 선택 value
    @State var selectedLine = 0             // line 선택 value
    
    @State var line: [Int] = [1, 2, 3, 4, 5, 6, 7, 8]
    
    @Binding var stationValue: String
    @Binding var lineValue: Int
    @Binding var timeValue: Int
    
    @State var buttonTitle = TimeSettingDB().queryDB().isEmpty ? "입력하기" : "수정하기"
    
    
    var filteredStatioins: [(String, Int)] {
        line23.map { ($0.name, $0.intValue1) }
            .filter { $0.1 == selectedLine + 1 }
            .sorted { $0.0 < $1.0 }
    }
    
    
    var body: some View {
            VStack(content: {
                
                //title
                Text(titleName)
                    .font(.custom("Tenada", size: 25).bold())
                    .padding(.top, 20)
                
                
                // ---------------- time picker -------------------
                Picker("", selection: $selectedTime, content: {
                    ForEach(0..<timeList.count, id:\.self, content: { index in
                        Text("\(timeList[index])시").tag(index)
                            .font(.custom("Tenada", size: 25))
                    })
                })
                .pickerStyle(.wheel)
                
                // ---------------- 변경 button -------------------
                Button(buttonTitle, action: {
                    infoList = dbModel.queryDB()
                    
                    // 시간 설정 정보가 없을 때 => insert
                    if infoList.isEmpty {
                        alertType = .add
                        
                    } else {
                        alertType = .update
                    }
                }) // Button
                
                .font(.custom("Tenada", size: 20))
                .buttonStyle(.bordered)
                .buttonBorderShape(.capsule)
                .background(Color("toolbarColor"))
                .cornerRadius(30)
                .controlSize(.large)
                .foregroundColor(.black)
                .frame(width: 200, height: 50) // 버튼의 크기 조정
                .padding(.top, 40)
                
//                .tint(.black)
                .alert(item: $alertType) { alertType in
                    switch alertType {
                    case .add:
                        return Alert(
                            title: Text("알림"),
                            message: Text("\(timeList[selectedTime])시로 \n 설정하시겠습니까?"),
                            primaryButton: .destructive(Text("확인"), action: {
                                dbModel.insertDB(time: timeList[selectedTime], station: filteredStatioins[selectedStation].0, line: line[selectedLine])
                                
                                // * Binding으로 전달된 변수 갱신
                                stationValue = filteredStatioins[selectedStation].0
                                lineValue = line[selectedLine]
                                timeValue = timeList[selectedTime]
                                
                                dismiss()
                            }),
                            secondaryButton: .cancel(Text("취소"))
                        )
                    case .update:
                        return Alert(
                            title: Text("알림"),
                            message: Text("\(timeList[selectedTime])시로 \n 설정하시겠습니까?"),
                            primaryButton: .destructive(Text("확인"), action: {
                                dbModel.updateDB(time: timeList[selectedTime], station: filteredStatioins[selectedStation].0, line: line[selectedLine], id: infoList[0].id)
                                
                                // * Binding으로 전달된 변수 갱신
                                stationValue = filteredStatioins[selectedStation].0
                                lineValue = line[selectedLine]
                                timeValue = timeList[selectedTime]

                                dismiss()
                            }),
                            secondaryButton: .cancel(Text("취소"))
                        )
                    }
                }
            })//VStack
            .onAppear{
                // SettingView에서 넘어오는 Line 값이 임의로 설정한 124일 경우, 1호선부터 조회되도록 selectedLine = 0 처리
                if lineValue == 124 {
                    selectedLine = 0 // 1호선부터 출력되도록
                } else {
                    selectedLine = lineValue - 1 // 0 : 1호선이므로 -1처리해줌
                    selectedStation = filteredStatioins.firstIndex { $0.0 == stationValue } ?? 0
                    selectedTime = timeList.firstIndex { $0 == timeValue } ?? 0
                }
                
                print("onAppear lineValue : ", lineValue)
                print("onAppear selectedLine : ", selectedLine)
                print("--------------------------------------")
                print("onAppear stationValue : ", stationValue)
                print("onAppear selectedStation : ", selectedStation)
            }
    }
}

enum SettingAlertType: Identifiable {
    case add
    case update
    
    var id: Int{
        hashValue
    }
}
#Preview {
    TimeSettingView(titleName: "테스트제목", stationValue: .constant("Initial Station Value"), lineValue: .constant(1), timeValue: .constant(1))
}
